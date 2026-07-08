---
id: UNC@20.15.2@MMLCommand@SET DNNREPLACEFUNC
type: MMLCommand
name: SET DNNREPLACEFUNC（设置DNN替换功能管理参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DNNREPLACEFUNC
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- DNN替换功能管理
status: active
---

# SET DNNREPLACEFUNC（设置DNN替换功能管理参数）

## 功能

**适用NF：AMF**

此命令用于设置DNN替换功能管理参数。

## 注意事项

- 下一次移动性流程生效

- DNN替换功能和本地专网分流功能互斥，请勿同时开启两个功能。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DNNREPLACESW |
| --- |
| NO |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNREPLACESW | DNN替换功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF是否支持DNN替换功能。当本参数设置为“YES（是）”时，如果PCF在AM策略中下发smfSelInfo，AMF将在后续的PDU会话建立流程中，向PCF获取DNN替换策略，使用PCF返回的替换DNN来进行SMF的服务发现和PDU会话建立。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：否<br>- “YES（是）”：是<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DNNREPLACEFUNC查询当前参数配置值。<br>配置原则：<br>该参数仅对非漫游用户生效，国际漫游用户和异网漫游用户暂不支持DNN替换功能。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNNREPLACEFUNC]] · DNN替换功能管理参数（DNNREPLACEFUNC）

## 使用实例

开通多园区就近功能时，需要设置AMF支持协议标准的DNN替换功能，执行如下命令：

```
SET DNNREPLACEFUNC:DNNREPLACESW=YES;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置DNN替换功能管理参数（SET-DNNREPLACEFUNC）_23623018.md`
