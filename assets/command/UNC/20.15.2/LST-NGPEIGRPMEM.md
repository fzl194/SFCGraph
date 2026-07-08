---
id: UNC@20.15.2@MMLCommand@LST NGPEIGRPMEM
type: MMLCommand
name: LST NGPEIGRPMEM（查询5G PEI组性能统计对象成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPEIGRPMEM
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

# LST NGPEIGRPMEM（查询5G PEI组性能统计对象成员）

## 功能

**适用NF：AMF**

该命令用于查询指定5G PEI组性能统计对象内的PEI成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGPEIGPN | NG PEI群组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于标识NG PEI组的性能统计对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。“NG PEI群组名称”已经通过ADD PERFNGPEIGRP配置。<br>默认值：无<br>配置原则：无 |
| PEITAC | PEI设备型号核准号码 | 可选必选说明：可选参数<br>参数含义：该参数用于标识用户的设备型号核准号码（TAC）。TAC由PEI的前8位数字组成，由欧洲型号认证中心分配，用来标识某一型号的手机。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是8。PEITAC编码为10进制数，按照字符串格式输入，字符串长度为8，只能由数字（0-9）组成。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NG PEI组性能统计对象成员（NGPEIGRPMEM）](configobject/UNC/20.15.2/NGPEIGRPMEM.md)

## 使用实例

查询PEI群组名称为“phone_xx”的成员记录：

```
%%LST NGPEIGRPMEM: NGPEIGPN="13", PEITAC="12345678";%%
RETCODE = 0  操作成功

结果如下
--------
      NG PEI群组名称  =  123/13
 PEI设备型号核准号码  =  12345678
        设备详细信息  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-PEI组性能统计对象成员（LST-NGPEIGRPMEM）_43079254.md`
