---
id: UNC@20.15.2@MMLCommand@LST NGTAIGRPMEM
type: MMLCommand
name: LST NGTAIGRPMEM（查询5G TAI组性能统计对象成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGTAIGRPMEM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# LST NGTAIGRPMEM（查询5G TAI组性能统计对象成员）

## 功能

**适用NF：AMF**

该命令用于查询指定5G TAI组性能统计对象内的TAI成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAIGPN | NG TAI组名 | 可选必选说明：可选参数<br>参数含义：该参数用于标识基于5G TAI组的性能统计对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写，不支持空格及“\”。5G TAI组性能统计对象名称通过ADD PERFNGTAIGROUP命令进行创建。<br>默认值：无<br>配置原则：无 |
| BGNTAI | 起始TAI | 可选必选说明：可选参数<br>参数含义：该参数用于表示TAI组所包含的TAI起始值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是11~12。TAI由MCC、MNC和TAC组成。其中MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度；TAC编码为16进制数，其固定为6位，若不足则左起补0。输入的起始TAI值必须小于或者等于结束TAI值。对于同一个5G TAI组性能统计对象，输入的起始TAI值和终止TAI值定义的TAI号段范围不允许与该对象其它记录定义的TAI号段范围相互交叉、包含或重合。<br>默认值：无<br>配置原则：无 |
| ENDTAI | 终止TAI | 可选必选说明：可选参数<br>参数含义：该参数用于表示TAI组所包含的TAI结束值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是11~12。TAI由MCC、MNC和TAC组成。其中MCC为3位数字，MNC为2个或者3位数字，填写时请遵循实际长度；TAC编码为16进制数，其固定为6位，若不足则左起补0。输入的终止TAI值必须大于或者等于起始TAI值。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G TAI组性能统计对象成员（NGTAIGRPMEM）](configobject/UNC/20.15.2/NGTAIGRPMEM.md)

## 使用实例

查询组名为“Hangzhou”的性能统计对象内的TAI成员，执行如下命令：

```
%%LST NGTAIGRPMEM:;%%
RETCODE = 0  操作成功

结果如下
--------
NG TAI组名  =  Hangzhou
   起始TAI  =  46000112233
   终止TAI  =  46000112233
(结果个数= 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-TAI组性能统计对象成员（LST-NGTAIGRPMEM）_96242272.md`
