---
id: UNC@20.15.2@MMLCommand@LST APNPAGINGPLCY
type: MMLCommand
name: LST APNPAGINGPLCY（查询APN寻呼策略参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNPAGINGPLCY
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 基于APN的寻呼策略配置
status: active
---

# LST APNPAGINGPLCY（查询APN寻呼策略参数配置）

## 功能

**适用网元：MME**

该命令用于查询APN寻呼策略参数配置。

## 注意事项

当不输入查询条件时，显示所有记录信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN网络标识。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- 每条记录中的“APNNI”字段不能重复。<br>- “APNNI”（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNPAGINGPLCY]] · APN寻呼策略参数配置（APNPAGINGPLCY）

## 使用实例

1.查询所有APN NI的属性信息：

LST APNPAGINGPLCY:;

```
%%LST APNPAGINGPLCY:;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
       APNNI  =  HUAWEI.COM
  寻呼优先级  =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN寻呼策略参数配置(LST-APNPAGINGPLCY)_26145712.md`
