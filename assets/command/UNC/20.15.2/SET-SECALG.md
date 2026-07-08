---
id: UNC@20.15.2@MMLCommand@SET SECALG
type: MMLCommand
name: SET SECALG（设置安全算法）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SECALG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 安全算法配置
status: active
---

# SET SECALG（设置安全算法）

## 功能

![](设置安全算法（SET SECALG）_01666249.assets/notice_3.0-zh-cn_2.png)

执行此命令将修改安全算法开关状态，开关开启后会导致环境启用不安全配置。

该命令用于设置建链时使用的安全算法的开关状态。开关打开时该算法可以使用，关闭时该算法被禁用。

## 注意事项

- 执行此命令关闭不安全配置时，请确认是否存在第三方设备对接场景。如果存在上述场景，关闭后可能会影响对接，请谨慎处理。
- 执行完本命令修改安全算法状态后请在OM Portal的“ 应用配置 > 服务治理 ”界面查询是否存在OMBrokerSvc服务，如果有则需要对该服务进行“批量复位”操作。
- 初始部署场景下开关默认为关闭状态，升级场景下开关状态保持不变。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALGTYPE | 算法类型 | 可选必选说明：必选参数<br>参数含义：安全算法类型。<br>取值范围：<br>DHE（DHE）<br>默认值：DHE（DHE）。<br>配置原则：无。 |
| SWITCHSTATE | 开关 | 可选必选说明：必选参数<br>参数含义：安全算法开关。<br>取值范围：<br>- ON（打开）<br>- OFF（关闭）<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECALG]] · 安全算法（SECALG）

## 使用实例

设置安全算法的开关状态。

```
%%SET SECALG: ALGTYPE=DHE, SWITCHSTATE=OFF;%%
RETCODE = 0  操作成功  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SECALG.md`
