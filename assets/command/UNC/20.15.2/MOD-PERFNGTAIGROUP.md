---
id: UNC@20.15.2@MMLCommand@MOD PERFNGTAIGROUP
type: MMLCommand
name: MOD PERFNGTAIGROUP（修改NG TAI组性能统计对象）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: PERFNGTAIGROUP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# MOD PERFNGTAIGROUP（修改NG TAI组性能统计对象）

## 功能

**适用NF：AMF**

该命令用于修改指定的NG TAI组性能统计对象信息。

## 注意事项

- 该命令执行后立即生效。

- 在执行本命令修改NGTAIGPN之前必须通过RMV NGTAIGRPMEM和RMV PERFRPTRANGE删除对本命令的NGTAIGPN参数的引用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAIGPIDX | NG TAI组索引 | 可选必选说明：必选参数<br>参数含义：NG TAI组对应的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~6000。<br>默认值：无<br>配置原则：无 |
| NGTAIGPN | NG TAI组名 | 可选必选说明：必选参数<br>参数含义：该参数用于标识基于5G TAI组的性能统计对象名称。5G TAI组内的TAI成员通过ADD NGTAIGRPMEM命令进行增加。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写，不支持空格及“\”且全局唯一。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NG TAI组性能统计对象（PERFNGTAIGROUP）](configobject/UNC/20.15.2/PERFNGTAIGROUP.md)

## 使用实例

将索引为1的NG TAI组名称修改为"huawei":

```
MOD PERFNGTAIGROUP: NGTAIGPIDX=1, NGTAIGPN="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改NG-TAI组性能统计对象（MOD-PERFNGTAIGROUP）_09653042.md`
