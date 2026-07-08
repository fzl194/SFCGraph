---
id: UNC@20.15.2@MMLCommand@ADD PERFNGTAIGROUP
type: MMLCommand
name: ADD PERFNGTAIGROUP（增加NG TAI组性能统计对象）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD PERFNGTAIGROUP（增加NG TAI组性能统计对象）

## 功能

**适用NF：AMF**

该命令用于手工增加NG TAI组性能统计对象的配置。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入6000条记录。
- 本命令实际允许配置的记录数同时受平台能力约束，估算公式为：实际允许配置的记录数=(700W*OMU个数-非TAI对象原始指标数)/USN POD个数/80个指标。当系统OMU个数为4个时，非TAI对象原始指标数为450W；当系统OMU个数为2个时，非TAI对象原始指标数为230W。USN POD的个数可以使用DSP POD命令查询，OMU个数可以使用DSP NODE命令查询。如果估算结果小于6000以估算结果为准，如果超过6000以6000为准。如果有疑问，请联系华为技术支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAIGPN | NG TAI组名 | 可选必选说明：可选参数<br>参数含义：该参数用于标识基于5G TAI组的性能统计对象名称。5G TAI组内的TAI成员通过ADD NGTAIGRPMEM命令进行增加。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写，不支持空格及“\”且全局唯一。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFNGTAIGROUP]] · NG TAI组性能统计对象（PERFNGTAIGROUP）

## 使用实例

添加一个组名为huawei的TAI组对象：

```
ADD PERFNGTAIGROUP: NGTAIGPN="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PERFNGTAIGROUP.md`
