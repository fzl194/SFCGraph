---
id: UDG@20.15.2@MMLCommand@DSP MSSPORTINFO
type: MMLCommand
name: DSP MSSPORTINFO（显示端口信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSPORTINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSPORTINFO（显示端口信息）

## 功能

该命令用于显示端口信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令不支持单条件查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务类型。 |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定微服务实例号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无<br>配置原则：使用<br>**[DSP PAENODE](../../服务通信管理/策略查询/显示PAE节点信息（DSP PAENODE）_92520008.md)**<br>查看工作角色为数据转发对应的微服务实例号。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSPORTINFO]] · 端口信息（MSSPORTINFO）

## 使用实例

显示端口信息：

```
DSP MSSPORTINFO:CELLTYPE="aa", CELLINSTANCE="bb";
```

```
RETCODE = 0  操作成功。

结果如下
--------------------------------- 
微服务类型   微服务实例号   端口号   端口名     PCI地址       驱动类型     设备类型    逻辑进程号  

aa           bb             2        uio1       0000:00:07.0  pmd          virtio       0                 
aa           bb             3        uio7       0000:00:08.0  pmd          virtio       0     
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSPORTINFO.md`
