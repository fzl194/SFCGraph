---
id: UNC@20.15.2@MMLCommand@LST NRFSCPDOMAINRT
type: MMLCommand
name: LST NRFSCPDOMAINRT（查询SCP Domain最长匹配后缀转发路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSCPDOMAINRT
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
- SCP Domain路由管理
status: active
---

# LST NRFSCPDOMAINRT（查询SCP Domain最长匹配后缀转发路由）

## 功能

**适用NF：NRF**

该命令用于查询基于SCP Domain的最长匹配后缀转发路由。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCPDOMAINSUFFIX | SCP Domain后缀 | 可选必选说明：可选参数<br>参数含义：该参数用于表示SCP Domain后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于SCP domain的最长后缀匹配寻址NF时的下一跳NRF实例组名称，即被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [SCP Domain最长匹配后缀转发路由（NRFSCPDOMAINRT）](configobject/UNC/20.15.2/NRFSCPDOMAINRT.md)

## 使用实例

执行以下命令，查询SCP Domain最长匹配后缀转发路由：

```
%%LST NRFSCPDOMAINRT:;%%
RETCODE = 0  操作成功

结果如下
--------
SCP Domain后缀  =  32123ASDF
 归属NRF组名称  =  azh0701
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCP-Domain最长匹配后缀转发路由（LST-NRFSCPDOMAINRT）_29461977.md`
