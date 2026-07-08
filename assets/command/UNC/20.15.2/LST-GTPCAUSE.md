---
id: UNC@20.15.2@MMLCommand@LST GTPCAUSE
type: MMLCommand
name: LST GTPCAUSE（查询GTP原因值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCAUSE
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 网关重选管理
- GTP原因值管理
status: active
---

# LST GTPCAUSE（查询GTP原因值）

## 功能

**适用网元：SGSN、MME**

此命令用于查询需要检测的PGW/GGSN返回的失败原因值。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVERSION | GTP版本 | 可选必选说明：可选参数<br>参数含义：待查询的原因值的所属GTP版本。<br>取值范围：<br>- “GTPV0V1（GTPv0v1）”：表示配置的原因值属于GTPv0v1。<br>- “GTPV2（GTPv2）”：表示配置的原因值属于GTPv2。<br>默认值：无 |
| REJCAUSE | 拒绝原因值 | 可选必选说明：可选参数<br>参数含义：待查询的拒绝原因值。SGW/PGW建立承载时，返回拒绝响应，该返回的原因值即拒绝原因值，指示系统异常或者资源受限。<br>取值范围：1~255<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCAUSE]] · GTP原因值（GTPCAUSE）

## 使用实例

查询GTP所有原因值：

LST GTPCAUSE:;

```
%%LST GTPCAUSE:;%%
RETCODE = 0  操作成功。

 操作结果如下
 --------------
 GTP版本  拒绝原因值                                              

 GTPv0v1        194                                    
 GTPv0v1        Service not supported(200)             
 GTPv0v1        226                                    
 GTPv0v1        Private Cause: GGSN not responding(240)
 GTPv2          64                                     
 GTPv2          No memory available(91)                
 GTPv2          112                          
(结果个数 = 7)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GTPCAUSE.md`
