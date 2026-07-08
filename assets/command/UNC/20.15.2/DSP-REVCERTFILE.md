---
id: UNC@20.15.2@MMLCommand@DSP REVCERTFILE
type: MMLCommand
name: DSP REVCERTFILE（查询证书吊销列表）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: REVCERTFILE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 证书维护
status: active
---

# DSP REVCERTFILE（查询证书吊销列表）

## 功能

本命令用于查询 OM Portal 内在 “ 安全 > 证书管理 > 证书吊销列表管理 ” 页面内显示的所有证书吊销列表。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| REVCERTFILE | 吊销列表名称 | 可选必选说明：可选参数<br>参数含义：吊销列表名称，支持模糊查询。<br>取值范围：字符串类型，输入长度范围为0~30。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@REVCERTFILE]] · 证书吊销列表（REVCERTFILE）

## 使用实例

查询证书吊销列表。

```
%%DSP REVCERTFILE: REVCERTFILE="root";%%
RETCODE = 0  操作成功

证书吊销列表名称  =  rootcrl
        创建时间  =  2021-06-28 14:04:16
          颁发者  =  CN=Huawei Root CA, O=Huawei, C=CN
        生效时间  =  2020-07-05 02:14:34
        失效时间  =  2021-08-07 02:30:35
        到期天数  =  40
        关联状态  =  已关联
        所属应用  =  superom04-v6
        场景名称  =  登录认证信任证书
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-REVCERTFILE.md`
