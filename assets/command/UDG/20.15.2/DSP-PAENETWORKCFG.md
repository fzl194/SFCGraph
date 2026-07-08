---
id: UDG@20.15.2@MMLCommand@DSP PAENETWORKCFG
type: MMLCommand
name: DSP PAENETWORKCFG（显示PAE网络配置信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PAENETWORKCFG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 系统资源
status: active
---

# DSP PAENETWORKCFG（显示PAE网络配置信息）

## 功能

该命令用于显示PAE网络配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看微服务实例号。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAENETWORKCFG]] · PAE网络配置信息（PAENETWORKCFG）

## 使用实例

查询微服务类型“aa”微服务实例“bb”的网络配置信息：

```
%%DSP PAENETWORKCFG: CELLTYPE="aa", CELLINSTANCE="bb";%%
RETCODE = 0  操作成功

结果如下:
-------------------------
微服务类型   微服务实例号 平面类型  组网类型  IP版本号  IP模式     报文是否转发到网关  封装类型
aa           bb           数据平面  L2        IPv4      SYSASSIGN  否                  UDP_LITE  
aa           bb           控制平面  L2        IPv4      SYSASSIGN  否                  UDP 
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PAENETWORKCFG.md`
