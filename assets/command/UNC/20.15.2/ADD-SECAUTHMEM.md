---
id: UNC@20.15.2@MMLCommand@ADD SECAUTHMEM
type: MMLCommand
name: ADD SECAUTHMEM（增加二次授权命令）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SECAUTHMEM
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 二次授权命令管理
status: active
---

# ADD SECAUTHMEM（增加二次授权命令）

## 功能

用于添加一条需要二次授权的MML命令。

二次授权功能开启后，对于需要进行二次授权的MML命令将需要输入可以二次授权的用户名和密码进行授权后，才能继续执行。

需要进行二次授权的MML命令可以通过 [LST SECAUTHMEM](查看二次授权命令（LST SECAUTHMEM）_88107917.md) 命令查询。

## 注意事项

- 网元ID必须在系统中存在。
- 命令名称和网元ID对应的MML命令必须存在。
- 该命令仅限具有Administrators角色的用户可以执行。在扩展域，仅限系统管理员可以执行。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数<br>参数含义：网元ID。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：无。 |
| COMMAND | 命令名称 | 可选必选说明：必选参数<br>参数含义：MML命令名称。<br>取值范围：长度不超过80的英文字符串。<br>默认值：无。<br>配置原则：无。 |
| TIPS | 提示信息 | 可选必选说明：可选参数<br>参数含义：命令提示信息。<br>取值范围：长度不超过512字节字符串。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SECAUTHMEM]] · 二次授权命令（SECAUTHMEM）

## 使用实例

新增需要二次授权的MML命令：

```
%%ADD SECAUTHMEM: MEID=0, COMMAND="LST ME";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SECAUTHMEM.md`
