# 显示SA Intelligence功能参数（LST AIFUNCPARA）

- [命令功能](#ZH-CN_CONCEPT_0000201793749057__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201793749057__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201793749057__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201793749057__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201793749057__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000201793749057__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201793749057)

**适用NF：PGW-U、UPF**

该命令用于查询SA intelligence功能参数。

#### [注意事项](#ZH-CN_CONCEPT_0000201793749057)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201793749057)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201793749057)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000201793749057)

假如运营商需要查询SA intelligence功能参数：

```
LST AIFUNCPARA:;
```

```

RETCODE = 0  操作成功

SA Intelligence功能参数
-----------------------
   SA Intelligence功能开关  =  不使能（关闭）
Intelligence验证流的抽样率  =  0
      Intelligence验证流数  =  2000
Intelligence验证流的有效率  =  9900
        SA协议解析加速开关  =  使能（开启）
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000201793749057)

参见SET AIFUNCPARA的参数说明。
