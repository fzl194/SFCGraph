---
id: UNC@20.15.2@MMLCommand@DSP MSSRULEM
type: MMLCommand
name: DSP MSSRULEM（显示匹配规则）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSRULEM
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSRULEM（显示匹配规则）

## 功能

该命令用于显示匹配规则。

用户设置规则后通过该命令进行查询当前的规则信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSSRULEM]] · 匹配规则（MSSRULEM）

## 使用实例

显示微服务类型为104的微服务实例csdb-pod-0172-16-0-247__103__0上的匹配规则：

```
%%DSP MSSRULEM: CELLTYPE="104", CELLINSTANCE="csdb-pod-0172-16-0-247__103__0";%%
RETCODE = 0  操作成功

结果如下:
---------
规则ID  偏移类型     引用计数  偏移  规则  掩码  

1       UFP包控制块  0         0     0000  ffff  
2       UFP包数据区  0         0     0000  ffff  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MSSRULEM.md`
