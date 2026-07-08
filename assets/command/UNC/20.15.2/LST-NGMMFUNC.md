---
id: UNC@20.15.2@MMLCommand@LST NGMMFUNC
type: MMLCommand
name: LST NGMMFUNC（查询5G移动性管理功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGMMFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- 5G移动性管理
status: active
---

# LST NGMMFUNC（查询5G移动性管理功能）

## 功能

**适用NF：AMF**

此命令用于查询移动性管理扩展功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGMMFUNC]] · 5G移动性管理功能（NGMMFUNC）

## 使用实例

查询移动性管理扩展功能，执行如下命令：

```
%%LST NGMMFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
                       AMF重选方式  =  重路由方式
                       最近访问TAI  =  是
                  RRC Inactive功能  =  是
                      发送网络信息  =  否
                     支持无N26接口  =  不支持
               支持通过NAS传短消息  =  不支持
              网络切片包含模式策略  =  标准模式
  3GPP接入方式下的网络切片包含模式  =  网络切片包含模式D
              是否允许紧急呼叫业务  =  NR接入的紧急呼叫回落
   基于UDM的P-CSCF Restoration功能  =  否
                      目标PLMN开关  =  是
                      全网跟踪开关  =  否
                  服务区域限制开关  =  否
              服务区域限制非标开关  =  否
根据签约分配Configured NSSAI的开关  =  否
              区域漫游限制优化开关  =  否
           互操作流程的AMF重选开关  =  关闭
           是否支持跨PLMN的SON流程  =  关闭
     AMF从UDM获取SMS签约数据的方式  =  SMS的签约与多个签约数据一起获取
               注册流程ODB限制策略  =  是
        PDU会话建立流程ODB限制策略  =  否
                       ODB限制策略  =  是
移动性管理流程中ODB是否限制PDU会话  =  否
  无用户上下文处理基站消息增强开关  =  关闭
          区域漫游限制功能增强开关  =  关闭
                  是否订阅位置上报  =  是
                      寻呼增强开关  =  关闭
                     MT服务SAR开关  =  关闭
              紧急呼叫类型携带策略  =  分开通知
                  漫游服务功能开关  =  关闭
                  RFSP变更通知开关  =  否
          网络投诉用户信息查询开关  =  否
           SelectedDNN携带策略开关  =  否
         已存在PDU会话建立使能开关  =  不支持
               NSA漫游接入功能开关  =  否
            获取上下文失败处理开关  =  否
                   RRC状态订阅类型  =  所有状态
       MEC本地专网分流策略信元开关  =  否
      ERROR INDICATION消息处理策略  =  未识别的用户NGAP索引
        基于区域的GUTI选网功能开关  =  否
              网络切片替换功能开关  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G移动性管理功能（LST-NGMMFUNC）_09653016.md`
