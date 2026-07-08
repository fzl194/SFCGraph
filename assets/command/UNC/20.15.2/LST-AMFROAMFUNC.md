---
id: UNC@20.15.2@MMLCommand@LST AMFROAMFUNC
type: MMLCommand
name: LST AMFROAMFUNC（查询AMF漫游功能管理参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFROAMFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF漫游功能控制
- AMF漫游功能管理
status: active
---

# LST AMFROAMFUNC（查询AMF漫游功能管理参数）

## 功能

**适用NF：AMF**

此命令用于查询AMF漫游功能管理参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFROAMFUNC]] · AMF漫游功能管理参数（AMFROAMFUNC）

## 使用实例

查询AMF漫游功能管理参数，执行如下命令：

```
%%LST AMFROAMFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
                      签约区域限制信息是否生效  =  否
N2切换源侧AMF签约区域限制信息是否在目标AMF生效  =  否
                切换流程源侧AMF是否携带SRVPLMN  =  是
               目标侧AMF识别跨PLMN切换流程方法  =  优先使用servingNetwork信元
     Inter移动性流程源侧AMF是否释放LBO模式会话  =  是
                      漫游场景通信FQDN检查开关  =  否
              漫游场景通信无FQDN注册拒绝原因值  =  15	
                              否携带V-GMLC地址  =  否	
                              V-GMLC客户端类型  =  不使用ClientType发现V-GMLC						  
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF漫游功能管理参数（LST-AMFROAMFUNC）_69427700.md`
