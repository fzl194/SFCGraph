---
id: UDG@20.15.2@MMLCommand@DSP PAESCHEDULE
type: MMLCommand
name: DSP PAESCHEDULE（显示PAE调度统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PAESCHEDULE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- PAE统计信息
status: active
---

# DSP PAESCHEDULE（显示PAE调度统计信息）

## 功能

该命令用于显示PAE调度统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |
| SCHEDULETYPE | 统计类型 | 可选必选说明：必选参数<br>参数含义：统计类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- port：端口调度统计。<br>- queue：队列调度统计。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAESCHEDULE]] · PAE调度统计信息（PAESCHEDULE）

## 使用实例

显示PAE端口调度统计信息，统计类型为端口调度统计：

```
DSP PAESCHEDULE: CELLTYPE="aa", CELLINSTANCE="bb",SCHEDULETYPE=port;
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
名称  ID   调度次数   有效调度次数  接收缓存区满的次数  平均批量收包数  平均批量发包数  获取锁失败次数  队列ID  

eth4  0x2  166753700  2033119       0                   2               13              0               0
eth5  0x3  163311221  1258876       0                   1               13              0               0
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示PAE调度统计信息（DSP-PAESCHEDULE）_92520041.md`
