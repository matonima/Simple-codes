{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled2",
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyOdpviBCwVuGUXhIvbb+SO/",
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
        "<a href=\"https://colab.research.google.com/github/matonima/Simple-codes/blob/main/strings%20of%20word%20in%20dictionary.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#given a dictionary of words and a large input string. You have to find out whether the input string can be completely segmented into the words of a given dictionary\n",
        "def can_segment_string(s, dictionary):\n",
        "  if (len(s))!=0:\n",
        "    if s in dictionary:\n",
        "      y=1\n",
        "    else:\n",
        "      y=0\n",
        "  return (y==1)\n",
        "dict1=\"apple\",\"pie\",\"not\",\"hi\"\n",
        "S=\"apple\"\n",
        "print(can_segment_string(S, dict1))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ee2262a9cO_9",
        "outputId": "01aafb87-eda9-4750-df9f-40966f2cabd7"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    }
  ]
}