---
id: UNC@20.15.2@MMLCommand@SET MONNFTHR
type: MMLCommand
name: SET MONNFTHR（设置正常状态网元的占比阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MONNFTHR
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET MONNFTHR（设置正常状态网元的占比阈值）

## 功能

该命令用于配置与当前网元具有容灾关系的其他网元中，状态正常的网元数目在所有网元数目的占比阈值。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NFNORMALTHR |
| --- |
| 100 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFNORMALTHR | 正常状态网元占比阈值（%） | 可选必选说明：可选参数<br>参数含义：当前网元具有容灾关系的其他网元中，状态正常的网元数目在所有网元数目的占比阈值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MONNFTHR查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [正常状态网元的占比阈值（MONNFTHR）](configobject/UNC/20.15.2/MONNFTHR.md)

## 使用实例

配置正常状态网元的占比阈值为100%。

```
%%SET MONNFTHR: NFNORMALTHR=100;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置正常状态网元的占比阈值（SET-MONNFTHR）_66605040.md`
