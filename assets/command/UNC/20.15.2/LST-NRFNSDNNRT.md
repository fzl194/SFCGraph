---
id: UNC@20.15.2@MMLCommand@LST NRFNSDNNRT
type: MMLCommand
name: LST NRFNSDNNRT（查询DNN和网络切片路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFNSDNNRT
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- DNN路由管理
status: active
---

# LST NRFNSDNNRT（查询DNN和网络切片路由）

## 功能

**适用NF：NRF**

该命令用于查询已配置的DNN和网络切片的路由信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数不区分大小写。<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为SMF的路由转发功能，其他NF类型为预留功能。 |
| SST | 切片服务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示切片服务类型，标识网络切片所具备的特性和服务类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片描述 | 可选必选说明：可选参数<br>参数含义：该参数用于表示切片描述，是对相同SST的网络切片实例的差异化描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是6。该参数只能由字母（A-F或者a-f）、数字（0-9）组成。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DNN和网络切片归属的NRF实例组名称，此NRF实例组作为当前NRF的下一跳路由，该参数需要输入时，可通过LST NRFGROUP命令获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNSDNNRT]] · DNN和网络切片路由（NRFNSDNNRT）

## 使用实例

- 查询所有DNN和网络切片的路由信息。
  ```
  LST NRFNSDNNRT:;
  %%LST NRFNSDNNRT:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  DNN         切片服务类型  切片描述   归属NRF组名称  

  dnn001      100           000fff     nrfgroup002          
  huawei.com  0             000001     nrfgroup002          
  (结果个数 = 2)

  ---    END
  ```
- 查询数据网络名称为huawei.com，切片服务类型为0，切片描述为000001，归属NRF组名称为nrfgroup001的路由信息。
  ```
  LST NRFNSDNNRT: DNN="huawei.com", SST=0, SD="000001", NEXTNRFGRPNAME="nrfgroup001";
  %%LST NRFNSDNNRT: DNN="huawei.com", SST=0, SD="000001", NEXTNRFGRPNAME="nrfgroup001";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                   DNN  =  huawei.com
          切片服务类型  =  0
              切片描述  =  000001
         归属NRF组名称  =  nrfgroup001
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNN和网络切片路由（LST-NRFNSDNNRT）_09654157.md`
