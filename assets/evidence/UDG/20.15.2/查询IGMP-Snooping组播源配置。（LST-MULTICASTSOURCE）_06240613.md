# 查询IGMP Snooping组播源配置。（LST MULTICASTSOURCE）

- [命令功能](#ZH-CN_CONCEPT_0000207006240613__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000207006240613__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000207006240613__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000207006240613__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000207006240613__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000207006240613__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000207006240613)

**适用NF：UPF**

该命令用于查询IGMP Snooping组播源配置。

#### [注意事项](#ZH-CN_CONCEPT_0000207006240613)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000207006240613)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000207006240613)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD NGVNINSTANCE命令配置生成。 |

#### [使用实例](#ZH-CN_CONCEPT_0000207006240613)

查询5G LAN组的N3侧的组播源：

```
LST MULTICASTSOURCE:;
```

```

%%LST MULTICASTSOURCE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
  5G LAN组名称  =  a0000001-460-003-01
     组播源类型  =  IMSI
           IMSI  =  217456789012353
 双发选收结对ID  =  0
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000207006240613)

参见ADD MULTICASTSOURCE的参数说明。
