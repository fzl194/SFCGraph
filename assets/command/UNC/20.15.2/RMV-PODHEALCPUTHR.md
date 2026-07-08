---
id: UNC@20.15.2@MMLCommand@RMV PODHEALCPUTHR
type: MMLCommand
name: RMV PODHEALCPUTHR（删除对应PODTYPE的配置记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PODHEALCPUTHR
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# RMV PODHEALCPUTHR（删除对应PODTYPE的配置记录）

## 功能

当前版本此命令可正常下发，但配置不生效。

该命令用于删除对应PODTYPE的配置记录。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | POD类型 | 可选必选说明：必选参数<br>参数含义：用于设置POD类型。可通过<br>[**DSP PODINFO**](../../编排管理/POD管理/显示已部署的Pod实例信息（DSP PODINFO）_09587375.md)<br>查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [对应PODTYPE下的阈值配置（PODHEALCPUTHR）](configobject/UNC/20.15.2/PODHEALCPUTHR.md)

## 使用实例

删除对应PODTYPE的配置记录

```
%%RMV PODHEALCPUTHR: PODTYPE="vha-pod";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除对应PODTYPE的配置记录（RMV-PODHEALCPUTHR）_24675206.md`
