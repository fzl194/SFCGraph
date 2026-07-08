---
id: UNC@20.15.2@MMLCommand@SET 5GGUMINFO
type: MMLCommand
name: SET 5GGUMINFO（设置灰度升级所处于的阶段）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: 5GGUMINFO
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 灰度升级管理
- 灰度升级批次
status: active
---

# SET 5GGUMINFO（设置灰度升级所处于的阶段）

## 功能

灰度升级流程中，执行此命令，用于设置灰度升级所处的阶段。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| STAGE |
| --- |
| PreUpgrade |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STAGE | 阶段 | 可选必选说明：必选参数<br>参数含义：该参数用于标识灰度升级所处的阶段。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [灰度升级所处于的阶段（5GGUMINFO）](configobject/UNC/20.15.2/5GGUMINFO.md)

## 使用实例

设置灰度升级阶段为InUpgrade：

```
%%SET 5GGUMINFO: STAGE="InUpgrade";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置灰度升级所处于的阶段（SET-5GGUMINFO）_34181853.md`
