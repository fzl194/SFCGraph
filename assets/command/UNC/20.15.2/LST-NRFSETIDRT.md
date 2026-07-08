---
id: UNC@20.15.2@MMLCommand@LST NRFSETIDRT
type: MMLCommand
name: LST NRFSETIDRT（查询NF Set ID最长匹配后缀转发路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSETIDRT
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- NF Set ID最长后缀匹配转发路由管理
status: active
---

# LST NRFSETIDRT（查询NF Set ID最长匹配后缀转发路由）

## 功能

**适用NF：NRF**

该命令用于查询基于NF Set ID的最长匹配后缀转发路由。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFSETIDSUFFIX | NF Set ID后缀 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF Set ID后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）、下划线（_）和点（.）组成，大小写不敏感，不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于NF Set ID的最长后缀匹配寻址NF时的下一跳NRF实例组名称，即被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSETIDRT]] · NF Set ID最长匹配后缀转发路由（NRFSETIDRT）

## 使用实例

查询基于NF Set ID的最长匹配后缀转发路由配置，执行如下命令：

```
LST NRFSETIDRT:;
%%LST NRFSETIDRT:;%%
RETCODE = 0  执行成功

操作结果如下:
-------------------------
NF Set ID后缀  =  NRF001
归属NRF组名称  =  asdf0701
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF-Set-ID最长匹配后缀转发路由（LST-NRFSETIDRT）_72758681.md`
