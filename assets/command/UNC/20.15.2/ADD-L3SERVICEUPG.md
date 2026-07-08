---
id: UNC@20.15.2@MMLCommand@ADD L3SERVICEUPG
type: MMLCommand
name: ADD L3SERVICEUPG（增加服务升级进度）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: L3SERVICEUPG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 灰度升级管理
- 服务升级进度
status: active
---

# ADD L3SERVICEUPG（增加服务升级进度）

## 功能

灰度升级中，执行此命令，用于添加新的服务升级进度。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入100000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L3SERVICE | L3Service | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个微服务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| POSITION | Position | 可选必选说明：必选参数<br>参数含义：该参数用于标识位于哪一层。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| MODE | Mode | 可选必选说明：必选参数<br>参数含义：该参数用于标识模式。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| STATUS | Status | 可选必选说明：必选参数<br>参数含义：该参数用于标识状态。<br>数据来源：本端规划<br>取值范围：<br>- PreUpgrade（PreUpgrade）<br>- InUpgrade（InUpgrade）<br>- PostUpgrade（PostUpgrade）<br>默认值：无<br>配置原则：无 |
| PROGRESS | Progress | 可选必选说明：必选参数<br>参数含义：该参数用于标识进度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/L3SERVICEUPG]] · 服务升级进度（L3SERVICEUPG）

## 使用实例

为服务AM增加新的升级进度：

```
%%ADD L3SERVICEUPG: L3SERVICE="AM", POSITION="Service", MODE="Gray", STATUS=PreUpgrade, PROGRESS=0;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加服务升级进度（ADD-L3SERVICEUPG）_33781925.md`
