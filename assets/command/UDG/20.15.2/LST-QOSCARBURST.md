---
id: UDG@20.15.2@MMLCommand@LST QOSCARBURST
type: MMLCommand
name: LST QOSCARBURST（查询用户做car的参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: QOSCARBURST
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 流量管理
- 配置Qos Car桶深信息
status: active
---

# LST QOSCARBURST（查询用户做car的参数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询用户流量管理时的突发尺寸（即令牌桶的深度）与流量速率的对应关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATE | Qos-Car速率（千比特/秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定速率，该参数一般由运营商规划给出。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [用户做car的参数（QOSCARBURST）](configobject/UDG/20.15.2/QOSCARBURST.md)

## 使用实例

查询用户配置的承载级流量做带宽管理的配置：

```
LST QOSCARBURST:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
Qos-Car速率（千比特/秒）    突发尺寸类型    突发尺寸（字节）    自动计算时长（毫秒）

128                         自动计算        0                   1000                
512                         突发尺寸        5000                0                   
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询用户做car的参数（LST-QOSCARBURST）_82837684.md`
