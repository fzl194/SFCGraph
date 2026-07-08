---
id: UDG@20.15.2@MMLCommand@DSP MSSPMDMATCH
type: MMLCommand
name: DSP MSSPMDMATCH（显示端口报文匹配统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSPMDMATCH
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSPMDMATCH（显示端口报文匹配统计信息）

## 功能

显示端口报文匹配统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |
| PORTID | 端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示端口ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：使用<br>**[DSP MSSPORTINFO](显示端口信息（DSP MSSPORTINFO）_92520022.md)**<br>命令获取端口号。 |
| RXTXTYPE | 收发包类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示收包或发包。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- rx：接收报文统计。<br>- tx：发送报文统计。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSPMDMATCH]] · 端口报文匹配统计信息（MSSPMDMATCH）

## 使用实例

显示微服务类型为104的微服务实例csdb-pod-0172-16-0-247__103__0的发送报文统计信息：

```
%%DSP MSSPMDMATCH: CELLTYPE="104", CELLINSTANCE="csdb-pod-0172-16-0-247__103__0", PORTID=2, RXTXTYPE=rx;%%
RETCODE = 0  操作成功

结果如下:
---------
      匹配规则ID  =  --
        开关状态  =  enable
 记录时间（min）  =  30
        匹配计数  =  607
记录报文功能使能  =  False
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示端口报文匹配统计信息（DSP-MSSPMDMATCH）_32309725.md`
