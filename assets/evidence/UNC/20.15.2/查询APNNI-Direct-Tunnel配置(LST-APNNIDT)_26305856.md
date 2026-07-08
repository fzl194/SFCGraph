# 查询APNNI Direct Tunnel配置(LST APNNIDT)

- [命令功能](#ZH-CN_MMLREF_0000001126305856__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305856__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305856__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305856__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305856__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305856__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305856__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305856)

**适用网元：SGSN**

此命令用于查询APNNI DT属性信息表中的某个APNNI的DT属性信息。

#### [注意事项](#ZH-CN_MMLREF_0000001126305856)

- 此命令执行后立即生效。
- 用户要使用DT功能还需满足RNC、GGSN和IMSI支持DT功能。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305856)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305856)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305856)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定启用基于APNNI的DT功能的APNNI。<br>取值范围：1～62位字符串<br>默认值：无<br>说明：“APNNI”<br>（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A~Z或a~z、数字0~9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。“*”表示通配符，如果用户使用的APNNI在配置表中无法匹配到对应的记录，则查询“*”通配符对应的配置记录。如果查询成功则使用“*”对应的配置；如果查询失败，则默认支持DT。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305856)

查询某个APNNI的DT属性记录：

LST APNNIDT: APNNI="huawei.com";

```
%%LST APNNIDT: APNNI="huawei.com";%%
RETCODE = 0  操作成功。

APNNI DT属性配置列表
--------------------
            APNNI  =  HUAWEI.COM
启用Direct Tunnel  =  是
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305856)

参见 [**ADD APNNIDT**](增加APNNI Direct Tunnel配置(ADD APNNIDT)_72345645.md) 命令的参数说明。
