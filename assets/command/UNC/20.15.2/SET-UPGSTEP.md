---
id: UNC@20.15.2@MMLCommand@SET UPGSTEP
type: MMLCommand
name: SET UPGSTEP（设置灰度升级pod滚动步长）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: UPGSTEP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 灰度升级管理
- 灰度升级步长
status: active
---

# SET UPGSTEP（设置灰度升级pod滚动步长）

## 功能

灰度升级流程中，执行此命令，用于设置灰度升级Pod滚动步长。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PODTYPE | REDUNDANCY |
| --- | --- |
| Service | 25 |
| Link | 25 |
| Lbf | 25 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | POD类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识升级时pod类型。<br>数据来源：本端规划<br>取值范围：<br>- Service（业务服务）<br>- Link（链路类服务）<br>- Lbf（LBF）<br>默认值：无。<br>配置原则：无 |
| REDUNDANCY | 冗余资源比例 | 可选必选说明：可选参数<br>参数含义：该参数用于标识资源冗余百分比。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPGSTEP查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [灰度升级Pod滚动步长（UPGSTEP）](configobject/UNC/20.15.2/UPGSTEP.md)

## 使用实例

设置灰度升级中业务服务类Pod的冗余资源比例为50%：

```
%%SET UPGSTEP: PODTYPE=Service, REDUNDANCY=50;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置灰度升级pod滚动步长（SET-UPGSTEP）_88502330.md`
