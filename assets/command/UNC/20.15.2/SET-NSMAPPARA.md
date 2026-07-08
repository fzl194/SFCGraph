---
id: UNC@20.15.2@MMLCommand@SET NSMAPPARA
type: MMLCommand
name: SET NSMAPPARA（设置网络切片映射相关参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NSMAPPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片映射管理
- 网络切片映射控制参数
status: active
---

# SET NSMAPPARA（设置网络切片映射相关参数）

## 功能

**适用NF：AMF**

该命令用于设置网络切片映射相关参数。

## 注意事项

- 该命令执行后立即生效。

- ADD NSMAPPARABYPLMN配置的网络切片映射参数优先级高于本命令配置的网络切片映射参数。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LOCALNSMAPSW | CFGNSENCSW | STANDARDNSSW |
| --- | --- | --- |
| ON | ON | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALNSMAPSW | 本地切片映射开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF是否为UE提供本地切片映射服务。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSMAPPARA查询当前参数配置值。<br>配置原则：<br>如果运营商希望始终通过NSSF为漫游用户提供切片映射服务，则此参数应该设置为“OFF”。<br>当此参数设置为“ON”时，如果AMF根据“本地切片映射配置命令（ADD AMFROAMNSMAP）”判断不能为UE的所有切片完成本地切片映射时，仍会发起到NSSF的网络切片映射流程。 |
| CFGNSENCSW | 漫游用户CFG切片增强功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制当漫游用户在Registration Request消息中Requested NSSAI信元携带的切片映射关系与核心网不一致或者未携带映射关系时，AMF在Registration Accept消息中是否下发Configured NSSAI。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSMAPPARA查询当前参数配置值。<br>配置原则：<br>3GPP协议仅要求在签约切片变更或者用户在Registration Request中携带Default configured NSSAI indication时才下发Configured NSSAI。当前参数控制的场景下发Configured NSSAI为非标实现。<br>当用户携带的切片映射关系不正确时，AMF下发Configured NSSAI给UE，可以及时让用户获取到全量签约切片在本网的映射关系。 |
| STANDARDNSSW | 标准切片映射开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF是否支持标准切片映射功能。<br>标准切片定义：SST为0~127，SD为空或者0xFFFFFF。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSMAPPARA查询当前参数配置值。<br>配置原则：<br>如果运营商期望本AMF为漫游用户提供标准切片映射功能，则此参数应该设置为“ON”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSMAPPARA]] · 网络切片映射相关参数（NSMAPPARA）

## 使用实例

打开本地切片映射开关和漫游用户CFG切片增强功能开关，执行如下命令：

```
SET NSMAPPARA: LOCALNSMAPSW=ON, CFGNSENCSW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NSMAPPARA.md`
