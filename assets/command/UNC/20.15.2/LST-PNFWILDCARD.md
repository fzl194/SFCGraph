---
id: UNC@20.15.2@MMLCommand@LST PNFWILDCARD
type: MMLCommand
name: LST PNFWILDCARD（查询对端NF的通配策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFWILDCARD
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端NF通配策略管理
status: active
---

# LST PNFWILDCARD（查询对端NF的通配策略）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于查询对端NF的通配策略。指定NFType时，输出该对端NF的对应通配策略。不指定NFType时，输出所有对端NF的通配策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- “NfInvalid（NfInvalid）”：NfInvalid<br>- “NfNRF（NfNRF）”：NfNRF<br>- “NfUDM（NfUDM）”：NfUDM<br>- “NfAMF（NfAMF）”：NfAMF<br>- “NfSMF（NfSMF）”：NfSMF<br>- “NfAUSF（NfAUSF）”：NfAUSF<br>- “NfNEF（NfNEF）”：NfNEF<br>- “NfPCF（NfPCF）”：NfPCF<br>- “NfSMSF（NfSMSF）”：NfSMSF<br>- “NfNSSF（NfNSSF）”：NfNSSF<br>- “NfUDR（NfUDR）”：NfUDR<br>- “NfLMF（NfLMF）”：NfLMF<br>- “NfGMLC（NfGMLC）”：NfGMLC<br>- “Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR<br>- “NfSEPP（NfSEPP）”：NfSEPP<br>- “NfUPF（NfUPF）”：NfUPF<br>- “NfN3IWF（NfN3IWF）”：NfN3IWF<br>- “NfAF（NfAF）”：NfAF<br>- “NfUDSF（NfUDSF）”：NfUDSF<br>- “NfBSF（NfBSF）”：NfBSF<br>- “NfCHF（NfCHF）”：NfCHF<br>- “NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS<br>- “NfSCP（NfSCP）”：NfSCP<br>- “NfPCSCF（NfPCSCF）”：NfPCSCF<br>- “NfMBSMF（NfMBSMF）”：NfMBSMF<br>- “NfUDN（NfUDN）”：NfUDN<br>- “NfNWDAF（NfNWDAF）”：NfNWDAF<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFWILDCARD]] · 对端NF的通配策略（PNFWILDCARD）

## 使用实例

运营商A需要查询NFTYPE为NfSMF的对端NF的通配策略。

```
%%LST PNFWILDCARD: NFTYPE=NfSMF;%%
RETCODE = 0  操作成功

结果如下
--------
                       NF类型  =  NfSMF
             非漫游SUPI配置通配开关  =  OFF
             非漫游SUPI缓存通配开关  =  ON
	       漫游SUPI配置通配开关  =  OFF
	       漫游SUPI缓存通配开关  =  ON
             非漫游GPSI配置通配开关  =  OFF
             非漫游GPSI缓存通配开关  =  ON
	       漫游GPSI配置通配开关  =  OFF
	       漫游GPSI缓存通配开关  =  ON
              非漫游TAI配置通配开关  =  ON
              非漫游TAI缓存通配开关  =  ON
	        漫游TAI配置通配开关  =  ON
	        漫游TAI缓存通配开关  =  ON
             非漫游PLMN配置通配开关  =  ON
             非漫游PLMN缓存通配开关  =  ON
	       漫游PLMN配置通配开关  =  ON
	       漫游PLMN缓存通配开关  =  ON
              非漫游DNN配置通配开关  =  ON
              非漫游DNN缓存通配开关  =  ON
		漫游DNN配置通配开关  =  ON
		漫游DNN缓存通配开关  =  ON
      非漫游WildcardDnn配置通配开关  =  OFF
      非漫游WildcardDnn缓存通配开关  =  OFF
        漫游WildcardDnn配置通配开关  =  OFF
        漫游WildcardDnn缓存通配开关  =  OFF
               非漫游NS配置通配开关  =  ON
               非漫游NS缓存通配开关  =  ON
		 漫游NS配置通配开关  =  ON
		 漫游NS缓存通配开关  =  ON
非漫游Routing Indicator配置通配开关  =  ON
非漫游Routing Indicator缓存通配开关  =  ON
  漫游Routing Indicator配置通配开关  =  ON
  漫游Routing Indicator缓存通配开关  =  ON
             CLIENTTYPE配置通配开关  =  ON
             CLIENTTYPE缓存通配开关  =  ON
          非漫游GROUPID配置通配开关  =  ON
          非漫游GROUPID缓存通配开关  =  ON
	    漫游GROUPID配置通配开关  =  ON
            漫游GROUPID缓存通配开关  =  ON
           非漫游服务区配置通配开关  =  ON
	     漫游服务区配置通配开关  =  ON
			
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFWILDCARD.md`
