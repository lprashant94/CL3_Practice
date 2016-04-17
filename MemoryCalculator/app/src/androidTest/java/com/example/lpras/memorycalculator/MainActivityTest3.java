package com.example.lpras.memorycalculator;

import junit.framework.TestCase;

/**
 * Created by lpras on 4/16/2016.
 */
public class MainActivityTest3 extends TestCase {

    public void testOnCreate() throws Exception {
MainActivity mainActivity=new MainActivity();

assertEquals(mainActivity.prev, 0);

    }
}