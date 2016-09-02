<?php
// src/AppBundle/Entity/Utterance.php
namespace AppBundle\Entity;

use Symfony\Component\Security\Core\User\UserInterface;

class Utterance
{

    private $text;

    // other properties and methods

    public function getText()
    {
        return $this->text;
    }

    public function setText($text)
    {
        $this->text = $text;
    }


}
