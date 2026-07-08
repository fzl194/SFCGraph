---
id: UNC@20.15.2@MMLCommand@LST PERFNGTAIGROUP
type: MMLCommand
name: LST PERFNGTAIGROUP（查询NG TAI组性能统计对象）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFNGTAIGROUP
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# LST PERFNGTAIGROUP（查询NG TAI组性能统计对象）

## 功能

**适用NF：AMF、SMF**

该命令用于查询NG TAI组性能统计对象信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAIGPN | NG TAI组名 | 可选必选说明：可选参数<br>参数含义：NG TAI组对外呈现的性能统计名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写，不支持空格及“\”且全局唯一。<br>默认值：无<br>配置原则：无 |
| NGTAIGPTYPE | NG TAI组类型 | 可选必选说明：可选参数<br>参数含义：NG TAI组测量对象的类型。<br>数据来源：本端规划<br>取值范围：<br>- “Manual（手动配置）”：手动配置<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFNGTAIGROUP]] · NG TAI组性能统计对象（PERFNGTAIGROUP）

## 使用实例

查询系统配置的所有NG TAI组信息

```
%%LST PERFNGTAIGROUP:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
 NG TAI Group Index  =  1
 NG TAI Group Name  =  huawei
 NG TAI Group Type  =  Manual Configuration
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PERFNGTAIGROUP.md`
