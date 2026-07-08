---
id: UDG@20.15.2@MMLCommand@LST PBUFREUSE5GC
type: MMLCommand
name: LST PBUFREUSE5GC（查询pbuf重用检测开关状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PBUFREUSE5GC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
- PBUF
status: active
---

# LST PBUFREUSE5GC（查询pbuf重用检测开关状态）

## 功能

该命令用于查询MSS服务的pbuf重用检测开关状态。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | pod类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定pod类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |
| POOLNAME | 内存池名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定内存池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PBUFREUSE5GC]] · pbuf重用检测开关设置（PBUFREUSE5GC）

## 使用实例

查询MSS服务的PAE内存池pbuf重用检测开关状态：

```
%%LST PBUFREUSE5GC: PODTYPE="isu-pod",POOLNAME="PAE";%%
RETCODE = 0  操作成功

结果如下
--------
   pod类型  =  isu-pod
内存池名称  =  PAE
  开关标记  =  开关关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PBUFREUSE5GC.md`
