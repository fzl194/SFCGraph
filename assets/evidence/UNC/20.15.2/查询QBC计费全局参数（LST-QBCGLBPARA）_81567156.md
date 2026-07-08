# 查询QBC计费全局参数（LST QBCGLBPARA）

- [命令功能](#ZH-CN_MMLREF_0000001181567156__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001181567156__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001181567156__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001181567156__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001181567156__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001181567156)

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询QBC计费全局参数。

## [注意事项](#ZH-CN_MMLREF_0000001181567156)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001181567156)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001181567156)

无

## [使用实例](#ZH-CN_MMLREF_0000001181567156)

查询QBC计费全局参数：

```
%%LST QBCGLBPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
 激活阶段QoSFlow上报模式  =  不上报
QoSFlow级Trigger填写方式  =  不使能
     QoSFlow时长计算方式  =  PACKETTRIGGERED
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001181567156)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 激活阶段QoSFlow上报模式 | 控制用户激活阶段是否上报QoSFlow信息给CHF。 |
| QoSFlow级Trigger填写方式 | 该参数用于设置当仅对PDU会话有效的Trigger发生时，生成的QFI容器是否携带同PDU会话一样的Trigger。 |
| QoSFlow时长计算方式 | 该参数用于设置CP指示UP QoSFlow的时长计费方式。 |
