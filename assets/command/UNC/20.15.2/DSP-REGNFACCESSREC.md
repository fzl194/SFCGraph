---
id: UNC@20.15.2@MMLCommand@DSP REGNFACCESSREC
type: MMLCommand
name: DSP REGNFACCESSREC（显示NF访问记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: REGNFACCESSREC
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF访问记录管理
status: active
---

# DSP REGNFACCESSREC（显示NF访问记录）

## 功能

**适用NF：NRF**

查询系统中已保存的NF在NRF上的访问记录。

若要查询系统中保存的所有NF在NRF上的访问记录，请不要输入任何参数。

若要查询特定访问类型的访问记录，请输入“访问类型”参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACCESSTYPE | 访问类型 | 可选必选说明：可选参数<br>参数含义：该参数表示NF的访问类型。<br>数据来源：本端规划<br>取值范围：<br>- REGISTER（注册）<br>- DEREGISTER（去注册）<br>- SUB（订阅）<br>- UPSUB（更新订阅）<br>- UNSUB（去订阅）<br>- UPDATE（全量更新）<br>- PATCH（部分更新）<br>- NOTIFY（订阅通知）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF访问记录（REGNFACCESSREC）](configobject/UNC/20.15.2/REGNFACCESSREC.md)

## 使用实例

- 当希望查询系统中保存的注册类型在NRF上的访问记录时，配置此命令。
  ```
  DSP REGNFACCESSREC:ACCESSTYPE=REGISTER;
  %%DSP REGNFACCESSREC: ACCESSTYPE=REGISTER;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  访问类型  访问时间                          NF类型  NF实例标识  订阅标识  其他信息  源IP地址       目的IP地址  用户代理            HTTP响应的via头域  报文长度(字节)  处理时延(毫秒)  响应结果  NF关键属性数量                                                                 Pod名称                   内部资源号

  注册      2020-10-17 11:00:04.08306279 +08  AMF     ff02-1      NULL      NULL      192.168.9.194  NULL        Go-http-client/2.0  NULL    672             1               201       NfStatus:register;SNssais(1);Tai(1);TaiRange(1);TotalNum:3;                    nrf-pod-6bc75768cb-6s86p  118
  注册      2020-10-17 11:15:38.969336564 +0  AMF     ff02-1      NULL      NULL      192.168.9.194  NULL        Go-http-client/2.0  NULL    672             3               201       NfStatus:register;SNssais(1);Tai(1);TaiRange(1);TotalNum:3;                    nrf-pod-6bc75768cb-6s86p  118
  注册      2020-10-17 11:03:48.324626402 +0  SMF     ff01-1      NULL      NULL      192.168.9.194  NULL        Go-http-client/2.0  NULL    1425            1               201       NfStatus:register;SNssais(1);Tai(2);TaiRange(2);DnnSmfInfoList(2);TotalNum:7;  nrf-pod-6bc75768cb-6s86p  78
  (结果个数 = 3)

  ---    END
  ```
- 当希望查询系统中保存的所有类型在NRF上的访问记录时，配置此命令。
  ```
  DSP REGNFACCESSREC:;
  %%DSP REGNFACCESSREC:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  访问类型  访问时间                          NF类型  NF实例标识  订阅标识                                  其他信息                                                   源IP地址       目的IP地址     用户代理            HTTP响应的via头域  报文长度(字节)  处理时延(毫秒)  响应结果  NF关键属性数量                                                                 Pod名称                   内部资源号

  订阅      2020-10-17 11:00:04.348097579 +0  AMF     NULL        0044001a65cda6d4bfef4865b1d6666395d4f3e7  http://192.168.9.194:5552/nnrf-nfm/v1/nf-instances/ff02-1  192.168.9.194  NULL           Go-http-client/2.0  NULL  0               2               201       NULL                                                                           nrf-pod-6bc75768cb-6s86p  68
  去订阅    2020-10-17 11:00:07.431575255 +0  NULL    NULL        0044001a65cda6d4bfef4865b1d6666395d4f3e7  NULL                                                       192.168.9.194  NULL           Go-http-client/2.0  NULL  0               0               204       NULL                                                                           nrf-pod-6bc75768cb-6s86p  68
  订阅      2020-10-17 11:03:48.558431697 +0  AMF     NULL        0044001a60066461bf4840e29ae71c29f768d76e  http://192.168.9.194:5552/nnrf-nfm/v1/nf-instances/ff02-1  192.168.9.194  NULL           Go-http-client/2.0  NULL  0               0               201       NULL                                                                           nrf-pod-6bc75768cb-6s86p  68
  更新订阅  2020-10-17 11:03:48.818431069 +0  AMF     NULL        0044001a60066461bf4840e29ae71c29f768d76e  NULL                                                       192.168.9.194  NULL           Go-http-client/2.0  NULL  0               0               200       NULL                                                                           nrf-pod-6bc75768cb-6s86p  68
  注册      2020-10-17 11:03:48.324626402 +0  SMF     ff01-1      NULL                                      NULL                                                       192.168.9.194  NULL           Go-http-client/2.0  NULL  1425            1               201       NfStatus:register;SNssais(1);Tai(2);TaiRange(2);DnnSmfInfoList(2);TotalNum:7;  nrf-pod-6bc75768cb-6s86p  78
  去注册    2020-10-17 11:03:49.022358689 +0  SMF     ff01-1      NULL                                      NULL                                                       192.168.9.194  NULL           Go-http-client/2.0  NULL  0               0               204       NULL                                                                           nrf-pod-6bc75768cb-6s86p  78
  订阅通知  2020-10-17 11:03:50.911243626 +0  AMF     ff01-1      0044001a60066461bf4840e29ae71c29f768d76e  http://192.168.9.194:5552/nnrf-nfm/v1/nf-instances/ff02-1  NULL           192.168.9.194  NULL                NULL  63              233             204       NULL                                                                           nrf-pod-6bc75768cb-6s86p  78
  (结果个数 = 7)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NF访问记录（DSP-REGNFACCESSREC）_09654174.md`
