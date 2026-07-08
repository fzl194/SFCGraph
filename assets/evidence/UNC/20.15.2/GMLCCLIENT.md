# 查询GMLC和LCS Client对照关系(LST GMLCCLIENT)

- [命令功能](#ZH-CN_MMLREF_0000001126145804__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145804__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145804__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145804__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145804__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145804__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145804__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145804)

**适用网元：SGSN**

此命令用于查询GMLC和LCS CLIENT对照表中的GMLC和LCS CLIENT的对照关系。不输入参数时将显示本SGSN下配置的所有GMLC和LCS CLIENT的对照关系。

#### [注意事项](#ZH-CN_MMLREF_0000001126145804)

- 此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145804)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145804)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145804)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTNUM | LCS客户端号码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LCS Client Number，是LCS客户端的E.164地址。<br>取值范围：1～16位十进制数字<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145804)

列出SGSN中所有存在的GMLC和LCS CLIENT的对照关系:

LST GMLCCLIENT:;

```
%%LST GMLCCLIENT:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
LCS客户端号码  =  861380123456789
     GMLC号码  =  861390123456789
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145804)

参见 [**ADD GMLCCLIENT**](增加GMLC和LCS Client对照关系(ADD GMLCCLIENT)_72225481.md) 的参数说明。
