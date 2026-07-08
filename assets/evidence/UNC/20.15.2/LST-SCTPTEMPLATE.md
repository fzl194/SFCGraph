# 查询SCTP模板（LST SCTPTEMPLATE）

- [命令功能](#ZH-CN_CONCEPT_0209897335__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897335__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897335__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897335__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897335__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897335__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897335)

**适用NF：PGW-C、SMF**

此命令用于查询SCTP模板。

#### [注意事项](#ZH-CN_CONCEPT_0209897335)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897335)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897335)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPTEMPLNAME | SCTP模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897335)

查询SCTP模板信息：

```
LST SCTPTEMPLATE: SCTPTEMPLNAME="sctp_tp1";
```

```

RETCODE = 0  操作成功

SCTP模板配置
------------
                      SCTP模板名称  =  sctp_tp1
SCTP发送心跳消息的间隔周期（毫秒）  =  30000
      SCTP耦联上消息重传的最大次数  =  5
    SCTP到特定IP消息重传的最大次数  =  4
                SCTP协议校验和算法  =  CRC32
                 拥塞状态门限（%）  =  60
             解除拥塞状态门限（%）  =  40
           SCTP Data Chunk传输模式  =  顺序传输
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897335)

参见ADD SCTPTEMPLATE的参数说明。
