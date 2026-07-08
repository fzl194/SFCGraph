---
id: UDG@20.15.2@MMLCommand@DSP SDRROUTE
type: MMLCommand
name: DSP SDRROUTE（查询SDRC中的APPROUTERINFO信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRROUTE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRROUTE（查询SDRC中的APPROUTERINFO信息）

## 功能

该命令用于查询SDRC中指定APP的ROUTE策略信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPINFO | APP信息 | 可选必选说明：必选参数<br>参数含义：该参数用于表示下发APPROUTE策略的APP信息，可通过<br>[**DSP SDRPOLICYKEYS**](显示SDRC中的策略Key信息（DSP SDRPOLICYKEYS）_22132897.md)<br>: POLICYTYPE=AppRoute;命令获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SDRC中的APPROUTERINFO信息（SDRROUTE）](configobject/UDG/20.15.2/SDRROUTE.md)

## 使用实例

使用如下命令查询SDRC中缓存的ROUTE策略信息：

```
%%DSP SDRROUTE: APPINFO=129;%%
RETCODE = 0  操作成功

结果如下
--------
                                             APP信息  =  129
                               APP将要发送的TOPIC ID  =  [40964 16387 4129 4135]
                                      APP订阅的TOPIC  =  [sub_topic_id:40961 key_type:2 ]
                                            路由算法  =  [key_type:2 endpoint_algo:<find_master:<> > ]
                                       第三方App标识  =  否
                第三方App和华为App之间的通信策略信息  =  <nil>
                         第三方App之间的通信策略信息  =  <nil>
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SDRC中的APPROUTERINFO信息（DSP-SDRROUTE）_94730433.md`
