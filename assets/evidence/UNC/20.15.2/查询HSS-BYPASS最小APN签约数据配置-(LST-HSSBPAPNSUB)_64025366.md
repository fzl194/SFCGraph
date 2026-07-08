# 查询HSS BYPASS最小APN签约数据配置 (LST HSSBPAPNSUB)

- [命令功能](#ZH-CN_CONCEPT_0000001264025366__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001264025366__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001264025366__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001264025366__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001264025366__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001264025366__1.3.6.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001264025366__1.3.7.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001264025366)

**适用网元：MME**

此命令用于查询最小APN签约数据群组对应的最小APN签约数据。

#### [注意事项](#ZH-CN_CONCEPT_0000001264025366)

无

#### [本地用户权限](#ZH-CN_CONCEPT_0000001264025366)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001264025366)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001264025366)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNSUBIDX | APN本地签约索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN本地签约数据索引。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001264025366)

查询HSS BYPASS最小APN签约数据配置，可以用如下命令：

LST HSSBPAPNSUB:;

```
%%LST HSSBPAPNSUB:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
      APN本地签约索引  =  0
                APNNI  =  12
              PDN类型  =  IPv4
上行APN AMBR （kbps）  =  400
下行APN AMBR （kbps）  =  500
           4-5G互操作  =  支持
                  QCI  =  2
           控制优先级  =  5
             计费属性  =  123
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001264025366)

参见 [ADD HSSBPAPNSUB](增加HSS BYPASS最小APN签约数据配置 (ADD HSSBPAPNSUB)_11385437.md) 的参数标识。
