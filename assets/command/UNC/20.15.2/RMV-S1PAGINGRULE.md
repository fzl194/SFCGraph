---
id: UNC@20.15.2@MMLCommand@RMV S1PAGINGRULE
type: MMLCommand
name: RMV S1PAGINGRULE（删除S1寻呼规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S1PAGINGRULE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1寻呼规则管理
status: active
---

# RMV S1PAGINGRULE（删除S1寻呼规则）

## 功能

**适用网元：MME**

此命令用于删除全部或者指定的S1寻呼规则。

## 注意事项

- 此命令执行后立即生效。
- 如果不输入任何参数，则提示：请输入"Rule Index"参数。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RECID | 规则索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待删除的S1寻呼规则的索引。<br>取值范围：1～1001<br>默认值：无<br>说明：当执行<br>[**ADD S1PAGINGRULE**](增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md)<br>命令增加S1寻呼规则时，系统会自动为该规则分配一个1～1001之间未使用的最小的索引，以唯一的标识该S1寻呼规则。可以通过<br>[**LST S1PAGINGRULE**](查询S1寻呼规则(LST S1PAGINGRULE)_72225927.md)<br>命令查询系统分配的索引值。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1PAGINGRULE]] · S1寻呼规则（S1PAGINGRULE）

## 使用实例

删除一条 “规则索引” 为 “1” 的S1寻呼规则：

```
RMV S1PAGINGRULE: RECID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除S1寻呼规则(RMV-S1PAGINGRULE)_72345847.md`
