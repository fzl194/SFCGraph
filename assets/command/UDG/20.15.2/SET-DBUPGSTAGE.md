---
id: UDG@20.15.2@MMLCommand@SET DBUPGSTAGE
type: MMLCommand
name: SET DBUPGSTAGE（设置CSDB灰度升级阶段）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DBUPGSTAGE
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 升级管理
status: active
---

# SET DBUPGSTAGE（设置CSDB灰度升级阶段）

## 功能

![](设置CSDB灰度升级阶段(SET DBUPGSTAGE)_32965409.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，正常状态下应尽量避免人工手动执行，如需使用请联系华为技术协助支持操作。

该命令用于设置CSDB灰度升级阶段，执行命令后CSDB会进入灰度升级模式。

## 注意事项

- 本命令目前仅提供给升级脚本在灰度升级过程中调用，正常状态下不建议操作员人工执行。
- 本命令目前所涉及的升级阶段存在默认排序，依次为稳态，整系统灰度升级开始，CSDB灰度升级开始，CSDB灰度升级结束，整系统灰度升级结束，其中系统初始阶段为稳态。
- 本命令执行时内部会判断所设置的阶段是否符合预期，若非预期则命令执行失败，具体规则如下：
    - 设置当前阶段的前序阶段时无任何限制，例如：若当前阶段为CSDB灰度升级开始，则设置该阶段之前的稳态或者整系统灰度升级开始阶段均会成功。
    - 设置当前阶段的后序阶段时需要保证阶段相邻，例如：若当前阶段为CSDB灰度升级开始，且要设置后序阶段时，设置CSDB灰度升级结束阶段会成功，而设置整系统灰度升级结束阶段则会返回失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| UPGSTAGE | 灰度升级阶段 | 可选必选说明：必选参数。<br>参数含义：该参数用于设置灰度升级阶段。可使用<br>**[LST DBUPGSTAGE](查询CSDB灰度升级阶段(LST DBUPGSTAGE)_33083965.md)**<br>命令查询当前的灰度升级阶段。<br>数据来源：本端规划。<br>取值范围：<br>- “稳态”：系统默认状态<br>- “整系统灰度升级开始”：灰度升级前准备<br>- “CSDB灰度升级开始”：灰度升级内部处理开始<br>- “CSDB灰度升级结束”：灰度升级内部处理结束<br>- “整系统灰度升级结束”：灰度升级完成<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DBUPGSTAGE]] · CSDB灰度升级阶段（DBUPGSTAGE）

## 使用实例

设置当前的 **“灰度升级阶段”** 为 **“CSDB灰度升级结束”** ：

```
%%SET DBUPGSTAGE: UPGSTAGE=CSDB_GRAY_UPGRADE_END;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-DBUPGSTAGE.md`
