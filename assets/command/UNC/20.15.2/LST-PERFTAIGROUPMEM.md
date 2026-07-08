---
id: UNC@20.15.2@MMLCommand@LST PERFTAIGROUPMEM
type: MMLCommand
name: LST PERFTAIGROUPMEM（查询TAI组性能统计对象成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFTAIGROUPMEM
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# LST PERFTAIGROUPMEM（查询TAI组性能统计对象成员）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询指定TAI组性能统计对象内的TAI成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TAIGROUPNAME | TAI组名 | 可选必选说明：可选参数<br>参数含义：该参数用于标识基于TAI组的性能统计对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写，不支持空格及“\”。 TAI组性能统计对象名称通过ADD PERFTAIGROUP命令创建。<br>默认值：无<br>配置原则：无 |
| BEGINTAI | 起始TAI | 可选必选说明：可选参数<br>参数含义：该参数用于表示TAI组所包含的TAI起始值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是9~12。TAI由MCC、MNC和TAC组成。其中MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度；TAC编码为16进制数，S1类型TAC固定为4位，若不足则左起补0；N2类型TAC固定为6位，若不足则左起补0。<br>默认值：无<br>配置原则：无 |
| ENDTAI | 终止TAI | 可选必选说明：可选参数<br>参数含义：该参数用于表示TAI组所包含的TAI结束值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是9~12。TAI由MCC、MNC和TAC组成。其中MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度；TAC编码为16进制数，S1类型TAC固定为4位，若不足则左起补0；N2类型TAC固定为6位，若不足则左起补0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFTAIGROUPMEM]] · TAI组性能统计对象成员（PERFTAIGROUPMEM）

## 使用实例

当需要查询所有TAI组性能统计对象成员，执行如下命令：

```
LST PERFTAIGROUPMEM:;
RETCODE = 0  操作成功。

结果如下
------------------------
  TAI组名  =  huawei
TAI组类型  =  S1TAC
  起始TAI  =  100000000
  终止TAI  =  10000FFFF
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PERFTAIGROUPMEM.md`
