<?php

// src/AppBundle/Controller/DialogsController.php
namespace AppBundle\Controller;

use Sensio\Bundle\FrameworkExtraBundle\Configuration\Route;
use Symfony\Bundle\FrameworkBundle\Controller\Controller;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\HttpFoundation\Request;
use AppBundle\Form\UtteranceType;
use AppBundle\Entity\Utterance;

class DialogsController extends Controller
{
    /**
     * @Route("dialogs/classify", name="dialogs_classify")
     */
    public function classifyAction(Request $request)
    {

        $utterance = new Utterance();
        $form = $this->createForm(UtteranceType::class, $utterance);
        $form->handleRequest($request);

        $result = "";
        if ($form->isSubmitted() && $form->isValid()) {

            $command = 'python2 /home/rdorado/project/dialogs/src/python/classify.py "'.$utterance->getText().'"';
            $resp = exec($command);
            $result = "Classification result: ".$resp;

        }


	return $this->render('dialogs/classify.html.twig', array(
            'result' => $result,
            'form' => $form->createView(),
        ));
    }

  

    
}
