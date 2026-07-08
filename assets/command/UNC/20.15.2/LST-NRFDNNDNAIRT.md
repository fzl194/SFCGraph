---
id: UNC@20.15.2@MMLCommand@LST NRFDNNDNAIRT
type: MMLCommand
name: LST NRFDNNDNAIRT（查询DNN中数据网络访问标识最长后缀匹配转发路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFDNNDNAIRT
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

# LST NRFDNNDNAIRT（查询DNN中数据网络访问标识最长后缀匹配转发路由）

## 功能

**适用NF：NRF**

该命令用于查询DNN中数据网络访问标识最长后缀匹配转发路由信息。该命令功能暂不生效。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示数据网络名称。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>取值为*时表示通配DNN。 |
| DNAISUFFIX | 数据网络访问标识后缀 | 可选必选说明：可选参数<br>参数含义：该参数用于表示数据网络访问标识后缀。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于DNN寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |
| NFTYPE | NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示通过DNN中数据网络访问标识最长后缀匹配转发路由寻址的NF类型。该参数功能暂不生效。<br>数据来源：本端规划<br>取值范围：<br>- SMF（SMF）<br>- UPF（UPF）<br>默认值：无<br>配置原则：<br>当前只支持NF类型为SMF的路由。 |

## 操作的配置对象

- [DNN中数据网络访问标识最长后缀匹配转发路由（NRFDNNDNAIRT）](configobject/UNC/20.15.2/NRFDNNDNAIRT.md)

## 使用实例

- 查询所有DNN中数据网络访问标识最长后缀匹配转发路由信息：
  ```
  LST NRFDNNDNAIRT:;
  %%LST NRFDNNDNAIRT:;%%
  RETCODE = 0  操作成功

  结果如下：
  ------------------------
          数据网络名称  =  ims
  数据网络访问标识后缀  =  huawei.com
         归属NRF组名称  =  L-NRF1
                NF类型  =  SMF
  (结果个数 = 1)
  ```
- 查询DNN为ims，DNAI为huawei.com的路由信息：
  ```
  LST NRFDNNDNAIRT: DNN="ims", DNAISUFFIX="huawei.com";
  %%LST NRFDNNDNAIRT: DNN="ims", DNAISUFFIX="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下：
  ------------------------
          数据网络名称  =  ims
  数据网络访问标识后缀  =  huawei.com
         归属NRF组名称  =  L-NRF1
                NF类型  =  SMF
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNN中数据网络访问标识最长后缀匹配转发路由（LST-NRFDNNDNAIRT）_92740998.md`
