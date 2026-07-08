---
id: UNC@20.15.2@MMLCommand@LST APNATSSSFUNC
type: MMLCommand
name: LST APNATSSSFUNC（查询APN ATSSS功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNATSSSFUNC
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- 基于APN的ATSSS功能控制
status: active
---

# LST APNATSSSFUNC（查询APN ATSSS功能）

## 功能

**适用NF：SMF**

该命令用于查询指定APN ATSSS功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [APN ATSSS功能（APNATSSSFUNC）](configobject/UNC/20.15.2/APNATSSSFUNC.md)

## 使用实例

查询指定APN下的ATSSS功能开关配置：

```
LST APNATSSSFUNC: APN="huawei.com";
%%LST APNATSSSFUNC: APN="huawei.com";%%
RETCODE = 0  操作成功

APN ATSSS功能参数
----------------------------
      APN名称  =  huawei.com
ATSSS功能开关  =  disable
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询APN-ATSSS功能（LST-APNATSSSFUNC）_96242064.md`
