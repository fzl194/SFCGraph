---
id: UNC@20.15.2@MMLCommand@SET CLTVFYSWITCH
type: MMLCommand
name: SET CLTVFYSWITCH（设置双向认证开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CLTVFYSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 代理管理
status: active
---

# SET CLTVFYSWITCH（设置双向认证开关）

## 功能

![](设置双向认证开关（SET CLTVFYSWITCH）_84238196.assets/notice_3.0-zh-cn_2.png)

执行该命令打开 “双向认证开关” 后可能会导致网管、三方平台断链，请谨慎操作。

此命令用于设置双向认证开关的开关状态。

## 注意事项

- 该命令仅限角色为Administrators的用户执行。
- 打开双向认证开关可能会导致网管、三方平台断链。需要在网管、三方平台上完成对接证书的上传。
- 双向认证开关默认关闭。
- 仅支持设置6443和9000端口的双向认证开关。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| PORT | 端口 | 可选必选说明：必选参数。<br>参数含义：双向认证的端口。<br>取值范围：6443，9000。<br>默认值：无。<br>配置原则：无。 |
| SWITCH | 开关 | 可选必选说明：必选参数。<br>参数含义：双向认证的开关状态，打开开关后，该端口会校验客户端证书。<br>取值范围：<br>- ON(开)<br>- OFF(关)<br>默认值：OFF(关)。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CLTVFYSWITCH]] · 双向认证开关（CLTVFYSWITCH）

## 使用实例

设置双向认证开关：

```
SET CLTVFYSWITCH: PORT=6443, SWITCH=OFF;
```

```
%%SET CLTVFYSWITCH: PORT=6443, SWITCH=OFF;%% 
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置双向认证开关（SET-CLTVFYSWITCH）_84238196.md`
