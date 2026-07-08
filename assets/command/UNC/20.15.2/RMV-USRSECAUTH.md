---
id: UNC@20.15.2@MMLCommand@RMV USRSECAUTH
type: MMLCommand
name: RMV USRSECAUTH（删除二次授权用户）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USRSECAUTH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 二次授权用户管理
status: active
---

# RMV USRSECAUTH（删除二次授权用户）

## 功能

用于取消用户的二次授权功能。

## 注意事项

- 用户名称必须已存在。
- 该命令仅限具有Administrators角色的用户可以执行。在扩展域，仅限系统管理员可以执行。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| USRNAME | 用户名称 | 可选必选说明：必选参数<br>参数含义：用户名称，在OM Portal的<br>“安全 > 用户管理”<br>或通过MML命令创建时的用户名称。<br>取值范围：长度不超过32个字符。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@USRSECAUTH]] · 二次授权用户（USRSECAUTH）

## 使用实例

删除二次授权用户：

```
%%RMV USRSECAUTH: USRNAME="test01";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-USRSECAUTH.md`
