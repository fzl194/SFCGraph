---
id: UNC@20.15.2@MMLCommand@DSP MSSFMMPROCESS
type: MMLCommand
name: DSP MSSFMMPROCESS（显示FMM的PBUF的进程信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSFMMPROCESS
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
status: active
---

# DSP MSSFMMPROCESS（显示FMM的PBUF的进程信息）

## 功能

该命令用于显示MSS的PBUF内存池内进程信息。

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

- [[configobject/UNC/20.15.2/MSSFMMPROCESS]] · FMM的PBUF的进程信息（MSSFMMPROCESS）

## 使用实例

显示类型为aa的微服务bb的MSS PBUF内存池内进程信息：

```
DSP MSSFMMPROCESS:CELLTYPE="aa", CELLINSTANCE="bb";
```

```
RETCODE = 0  操作成功。

结果如下
--------
内存池名称     进程号    逻辑进程号    该进程已占有的内存单元个数    该进程已使用的内存单元个数    该进程拥有的缓存中的剩余个数    泄露的内存单元个数    重用的内存单元个数    保留的内存单元个数

PAE            0         0             16388                         0                             16388                           0                     0                     0                 
PAE            254       254           0                             0                             0                               0                     0                     0                 
paeFmeaInfo    254       254           0                             0                             0                               0                     0                     0                 
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MSSFMMPROCESS.md`
