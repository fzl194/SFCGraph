---
id: UDG@20.15.2@MMLCommand@LST OSPFASBRSUMMARY
type: MMLCommand
name: LST OSPFASBRSUMMARY（查询引入路由聚合配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: OSPFASBRSUMMARY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF引入路由聚合配置
status: active
---

# LST OSPFASBRSUMMARY（查询引入路由聚合配置）

## 功能

该命令用于查询引入路由聚合配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无 |
| IPADDRESS | IP地址 | 可选必选说明：可选参数<br>参数含义：IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| ADDRESSMASK | 地址掩码 | 可选必选说明：可选参数<br>参数含义：地址掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFASBRSUMMARY]] · 引入路由聚合配置（OSPFASBRSUMMARY）

## 使用实例

查询引入路由聚合配置：

```
LST OSPFASBRSUMMARY:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                    进程号  =  1
                  拓扑标识  =  0
                    IP地址  =  10.2.2.0
                  地址掩码  =  255.255.255.0
      使能聚合路由的开销值  =  TRUE
            聚合路由的开销  =  100
      使能延迟发布聚合路由  =  TRUE
延迟发布聚合路由的时间（s） =  1000
                不发布路由  =  发布
        使能聚合路由的标记  =  TRUE
                  路由标签  =  0
              生成路由黑洞  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-OSPFASBRSUMMARY.md`
