---
id: UNC@20.15.2@MMLCommand@RMV BSSIDFORNSEI
type: MMLCommand
name: RMV BSSIDFORNSEI（删除NSEI和BSSID值的对应关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BSSIDFORNSEI
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- BSSID与NSEI映射值管理
status: active
---

# RMV BSSIDFORNSEI（删除NSEI和BSSID值的对应关系）

## 功能

**适用网元：SGSN**

此命令用于删除一个或一组NSEI和BSSID值的对应关系。只适用于Gb over IP自动配置的场景。

## 注意事项

- 此命令执行后立即生效。
- 此命令仅影响小部分话统，影响5个性能测量对象对应的性能测试指标，分别是“指定BSS附着”、“指定BSS SGSN内路由更新”、“指定BSS SGSN间路由更新”、“指定BSS无线资源”、“指定BSS GB接口流量”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | 起始NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的NSEI和BSSID值对应关系的网络服务实体起始标识。<br>取值范围：0～65535<br>默认值：无<br>说明：本参数为<br>[**ADD BSSIDFORNSEI**](增加NSEI和BSSID值的对应关系(ADD BSSIDFORNSEI)_72345595.md)<br>中存在的NSE起始标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BSSIDFORNSEI]] · NSEI和BSSID值的对应关系（BSSIDFORNSEI）

## 使用实例

删除一个或一组NSEI和BSSID值的对应关系，删除对应关系的 “NSE起始标识 ” 为 “0” ：

RMV BSSIDFORNSEI: NSEI=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-BSSIDFORNSEI.md`
