---
id: UNC@20.15.2@MMLCommand@DSP SECPOLICYAPPLNK
type: MMLCommand
name: DSP SECPOLICYAPPLNK（显示应用联动默认动作）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SECPOLICYAPPLNK
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略应用层联动默认动作
status: active
---

# DSP SECPOLICYAPPLNK（显示应用联动默认动作）

## 功能

该命令用于显示应用联动的缺省动作。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 策略编号 | 可选必选说明：必选参数<br>参数含义：策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECPOLICYAPPLNK]] · 应用联动默认动作（SECPOLICYAPPLNK）

## 使用实例

显示应用联动的缺省动作：

```
DSP SECPOLICYAPPLNK: SECPOLICYID=1;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
    策略编号  =  1
默认处理方式  =  传给CPU
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示应用联动默认动作（DSP-SECPOLICYAPPLNK）_50120690.md`
