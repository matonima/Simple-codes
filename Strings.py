{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled2.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyM2Fl7EHk9PA5bQKQ/Sartd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/matonima/Simple-codes/blob/main/Strings.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "T8mcHCw-Z1Dq",
        "outputId": "1331764f-d16e-446c-8d50-2e1e2f684599"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "dlrow olleh\n"
          ]
        }
      ],
      "source": [
        "#Reverse the order of words in a given sentence (an array of characters). Take the “Hello World” string for example\n",
        "def reverse(x):\n",
        "    if len(x)!=0:\n",
        "        y=x[::-1]\n",
        "        return y\n",
        "X=\"hello world\"\n",
        "Y=reverse(X)\n",
        "print(Y)"
      ]
    }
  ]
}